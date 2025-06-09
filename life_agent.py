def handle_life(message: str) -> str:
    # TODO: In final version this will query vector memory from your PDF
    if "yc" in message.lower():
        return "Your current YC fallback plan is to focus on pilot traction and update for the next batch."
    elif "new zealand" in message.lower():
        return "You planned to explore international versions of Plato while studying at AUT in NZ."
    else:
        return "This sounds like a personal reflection. Keep journaling — you’re on the right track."
