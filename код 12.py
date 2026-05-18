import tkinter as tk
from tkinter import ttk, messagebox
import json

MOVIES_FILE = 'movies.json'

def load_movies():
    try:
        with open(MOVIES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_movies(data):
    with open(MOVIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def validate_input():
    title = entry_title.get().strip()
    genre = entry_genre.get().strip()
    year = entry_year.get().strip()
    rating = entry_rating.get().strip()

    if not title or not genre:
        messagebox.showerror("Ошибка", "Название и жанр не должны быть пустыми.")
        return False

    if not year.isdigit() or not (1800 <= int(year) <= 2100):
        messagebox.showerror("Ошибка", "Год должен быть числом от 1800 до 2100.")
        return False

    try:
        rating_float = float(rating)
        if not (0 <= rating_float <= 10):
            messagebox.showerror("Ошибка", "Рейтинг должен быть числом от 0 до 10.")
            return False
    except ValueError:
        messagebox.showerror("Ошибка", "Рейтинг должен быть числом.")
        return False

    return True

def add_movie():
    if validate_input():
        movie = {
            "title": entry_title.get(),
            "genre": entry_genre.get(),
            "year": int(entry_year.get()),
            "rating": float(entry_rating.get())
        }
        movies.append(movie)
        save_movies(movies)
        refresh_table()
        clear_fields()

def refresh_table(filter_genre=None, filter_year=None):
    for item in tree.get_children():
        tree.delete(item)
    for movie in movies:
        if filter_genre and movie["genre"].lower() != filter_genre.lower():
            continue
        if filter_year and movie["year"] != int(filter_year):
            continue
        tree.insert("", "end", values=(movie["title"], movie["genre"], movie["year"], movie["rating"]))

def apply_filters():
    genre = entry_filter_genre.get().strip() if entry_filter_genre.get().strip() else None
    year = entry_filter_year.get().strip() if entry_filter_year.get().strip() else None
    refresh_table(genre, year)

def clear_fields():
    entry_title.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_rating.delete(0, tk.END)

