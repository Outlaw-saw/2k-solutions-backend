from enum import Enum


class UserRole(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"


class EnrollmentStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class ContactSubject(str, Enum):
    COURSE = "course"
    CORPORATE = "corporate"
    INTERNSHIP = "internship"
    PLACEMENT = "placement"
    OTHER = "other"


class MilestoneSection(str, Enum):
    HERO = "hero"
    MILESTONES = "milestones"
