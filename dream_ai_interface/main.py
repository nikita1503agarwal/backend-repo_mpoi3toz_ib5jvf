"""CLI interface for Dream.AI

Features:
- Infinite menu loop in main() with options: Image, Video, Transcription, Question, and q to quit
- afficher_menu(choix: str | None) -> str handles input or returns provided choice
- Separate functions for each menu action (menu_image, menu_video, menu_transcription, menu_question)
- Graceful handling of EOFError for non-interactive environments
- Bonus: Stylish title printed in the console

Run:
    python dream_ai_interface/main.py
"""
from __future__ import annotations

import sys
from typing import Optional

TITLE = "\U0001F3A8 DREAM.AI MENU \U0001F3A8"  # 🎨


def menu_image() -> str:
    """Placeholder for the Image feature."""
    message = "[Image] Fonction image appelée. (stub)"
    print(message)
    return message


def menu_video() -> str:
    """Placeholder for the Video feature."""
    message = "[Vidéo] Fonction vidéo appelée. (stub)"
    print(message)
    return message


def menu_transcription() -> str:
    """Placeholder for the Transcription feature."""
    message = "[Transcription] Fonction transcription appelée. (stub)"
    print(message)
    return message


def menu_question() -> str:
    """Placeholder for the Question feature."""
    message = "[Question] Fonction question appelée. (stub)"
    print(message)
    return message


def afficher_menu(choix: Optional[str] = None) -> str:
    """Affiche le menu et retourne le choix de l'utilisateur.

    If `choix` is provided, it is returned directly (used for tests).
    Otherwise, prompt the user via input(). Handles EOFError gracefully.

    Raises SystemExit if the user chooses 'q' to quit.
    """
    if choix is None:
        try:
            print("\n" + "=" * len(TITLE))
            print(TITLE)
            print("=" * len(TITLE))
            print("Choisissez une option :")
            print("  1. Image")
            print("  2. Vidéo")
            print("  3. Transcription")
            print("  4. Question")
            print("  q. Quitter")
            choix = input("> ").strip().lower()
        except EOFError:
            # In non-interactive environments, exit gracefully
            raise SystemExit(0)

    choix = choix.strip().lower()
    if choix == "q":
        print("Au revoir !")
        raise SystemExit(0)

    return choix


def main() -> None:
    """Boucle principale du programme CLI."""
    print("\n" + "=" * len(TITLE))
    print(TITLE)
    print("=" * len(TITLE))

    while True:
        try:
            choix = afficher_menu()
        except SystemExit as e:
            # Re-raise to exit program cleanly when 'q' or EOFError occurs
            raise

        if choix == "1":
            menu_image()
        elif choix == "2":
            menu_video()
        elif choix == "3":
            menu_transcription()
        elif choix == "4":
            menu_question()
        else:
            print("Choix invalide. Veuillez sélectionner 1, 2, 3, 4 ou q.")


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        # Allow clean exit without traceback
        sys.exit(e.code if isinstance(e.code, int) else 0)
