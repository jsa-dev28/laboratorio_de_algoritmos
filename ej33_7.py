from pathlib import Path
path = Path('gutenberg.txt')
contents = path.read_text(encoding="utf-8")
the = contents.lower().count('the ')
print(f"La palabra 'the' aparece {the} veces en el texto.")   