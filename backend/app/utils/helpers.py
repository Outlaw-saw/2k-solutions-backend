from typing import Any

from flask import request
from sqlalchemy import desc, asc
from sqlalchemy.orm import Query


def paginate(query: Query, page: int | None = None, per_page: int | None = None) -> dict[str, Any]:
    page = page or request.args.get("page", 1, type=int)
    per_page = per_page or request.args.get("per_page", 20, type=int)
    per_page = min(per_page, 100)

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "items": pagination.items,
        "meta": {
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total": pagination.total,
            "pages": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
        },
    }


def apply_sorting(query: Query, model: type, default_sort: str = "-created_at") -> Query:
    sort_param = request.args.get("sort", default_sort)
    order = desc if sort_param.startswith("-") else asc
    sort_field = sort_param.lstrip("-")
    if hasattr(model, sort_field):
        query = query.order_by(order(getattr(model, sort_field)))
    return query


def apply_search(query: Query, model: type, search_fields: list[str]) -> Query:
    search = request.args.get("search", "").strip()
    if search:
        filters = [getattr(model, f).ilike(f"%{search}%") for f in search_fields if hasattr(model, f)]
        if filters:
            from sqlalchemy import or_
            query = query.filter(or_(*filters))
    return query


def success_response(data: Any = None, message: str = "", meta: dict | None = None) -> dict:
    response: dict[str, Any] = {"success": True, "message": message, "data": data}
    if meta:
        response["meta"] = meta
    return response


def error_response(message: str = "", errors: list | None = None, status: int = 400) -> tuple:
    return {"success": False, "message": message, "errors": errors or [], "status": status}, status
