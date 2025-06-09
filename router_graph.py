from life_agent import handle_life
from restaurant_agent import handle_restaurant

def route_message(message: str) -> str:
    message_lower = message.lower()

    # Simple intent detection
    if any(keyword in message_lower for keyword in ["yc", "goal", "mental", "journal", "study", "reflection", "new zealand"]):
        return handle_life(message)
    elif any(keyword in message_lower for keyword in ["plato", "inventory", "supplier", "hiring", "restaurant", "staff", "stock"]):
        return handle_restaurant(message)
    else:
        return "I'm not sure if this is about your personal life or Manual AI. Try rephrasing!"
