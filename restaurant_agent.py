def handle_restaurant(message: str) -> str:
    if "plato" in message.lower():
        return "Plato is your voice-first table assistant for taking guest orders and syncing inventory."
    elif "inventory" in message.lower():
        return "Manual AI tracks ingredient stock and reorders with suppliers automatically."
    elif "supplier" in message.lower():
        return "Supplier bot handles low-stock alerts and order communication via Telegram."
    else:
        return "This sounds like a restaurant-related query. Try being more specific!"
