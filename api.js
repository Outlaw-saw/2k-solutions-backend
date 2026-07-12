const API_BASE = "https://twok-solutions-backend.onrender.com/api/v1";

async function api(path, options = {}) {
  const url = `${API_BASE}${path}`;
  const config = {
    headers: { "Content-Type": "application/json", ...options.headers },
    ...options,
  };
  const res = await fetch(url, config);
  const data = await res.json();
  if (!res.ok) throw new Error(data.message || "Request failed");
  return data;
}

function getToken() {
  return localStorage.getItem("access_token");
}

function setToken(token) {
  localStorage.setItem("access_token", token);
}

function clearToken() {
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
}

const AuthAPI = {
  register(body) {
    return api("/auth/register", { method: "POST", body: JSON.stringify(body) });
  },
  login(body) {
    return api("/auth/login", { method: "POST", body: JSON.stringify(body) });
  },
  me() {
    return api("/auth/me", { headers: { Authorization: `Bearer ${getToken()}` } });
  },
};

const ContactAPI = {
  submit(body) {
    return api("/contact", { method: "POST", body: JSON.stringify(body) });
  },
};

const ContentAPI = {
  courses() {
    return api("/courses");
  },
  services() {
    return api("/services");
  },
  testimonials() {
    return api("/testimonials");
  },
  faqs() {
    return api("/faqs");
  },
  technologies() {
    return api("/technologies");
  },
  steps() {
    return api("/steps");
  },
  differentiators() {
    return api("/differentiators");
  },
  stats() {
    return api("/stats");
  },
  siteSettings() {
    return api("/site");
  },
};
