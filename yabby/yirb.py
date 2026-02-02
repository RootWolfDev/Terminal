import requests
from rich import *
from rich.console import Console
import sys


def texirb():
    print(r"""
        .__      ___.    
 ___.__.|__|_____\_ |__  
<   |  ||  \_  __ \ __ \ 
 \___  ||  ||  | \/ \_\ \
 / ____||__||__|  |___  /
 \/                   \/ 
    """)


def yirb():
    console = Console()
    urnd = console.input("([green]yabby_irb[/])> ").strip()

    if urnd.lower() == "exit":
        print("Thanks for using my yirb !!")
        return False

    if not urnd.startswith("yirb "):
        print("[red]error!! use: yirb https://example.com/[/]")
        return True

    url_b = urnd.replace("yirb ", "").rstrip("/") + "/"

    try:
        ping = requests.get(url_b, timeout=5)
        if not (200 <= ping.status_code < 400):
            print("[red]url not reachable[/]")
            return True
    except requests.RequestException:
        print("[red]connection error[/]")
        return True

    print(f"[green]Scanning:[/] {url_b}")

    endpoints = [
        "index", "index.html", "index.php", "home", "main", "default",
        "welcome", "start", "landing", "portal",
        "login", "logout", "register", "signup", "signin", "auth",
        "password", "reset", "forgot", "verify",
        "dashboard", "admin", "admin/login", "admin/dashboard",
        "user", "users", "profile", "account", "settings", "preferences",
        "robots.txt", "sitemap.xml", "favicon.ico", "manifest.json",
        "humans.txt", "security.txt", "ads.txt", "app-ads.txt",
        ".well-known", ".well-known/security.txt",
        "api", "api/v1", "api/v2", "api/status", "api/docs",
        "api/swagger", "graphql", "rest", "webhook", "webhooks",
        "search", "filter", "browse", "categories", "tags",
        "posts", "articles", "news", "blog", "comments",
        "upload", "uploads", "download", "downloads", "files",
        "media", "images", "videos", "audio", "static",
        "contact", "about", "help", "support", "faq",
        "terms", "privacy", "policy", "legal", "copyright",
        "status", "health", "ping", "metrics", "monitor",
        "uptime", "logs", "errors", "debug", "test",
        "beta", "dev", "staging", "prod", "preview",
        "demo", "sandbox", "feedback", "reviews", "ratings","templates"
    ]

    for ep in endpoints:
        urlirb = url_b + ep
        try:
            r = requests.get(urlirb, timeout=5)
            if 200 <= r.status_code < 400:
                print(f"\n[green][+][/] found : {urlirb}")
            else:
                sys.stdout.write(f"\r[-] not found : {urlirb}")
                sys.stdout.flush() 
        except requests.RequestException:
            print(f"[red][-][/] error : {urlirb}")

    return True

def founction_b():
    while yirb():
        pass
