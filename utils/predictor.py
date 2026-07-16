import joblib
import pandas as pd
import numpy as np

# Load the trained pipeline only once
pipeline = joblib.load("model/House_price_pipeline.pkl")


def predict_house_price(form_data):
    """
    Predict house price using the trained pipeline.

    Parameters:
        form_data: request.form from Flask

    Returns:
        Formatted predicted house price
    """

    user_input = pd.DataFrame({

        "area": [int(form_data["area"])],
        "bedrooms": [int(form_data["bedrooms"])],
        "bathrooms": [int(form_data["bathrooms"])],
        "stories": [int(form_data["stories"])],
        "main_road": [form_data["main_road"]],
        "guest_room": [form_data["guest_room"]],
        "basement": [form_data["basement"]],
        "hot_water_heating": [form_data["hot_water_heating"]],
        "air_conditioning": [form_data["air_conditioning"]],
        "parking": [int(form_data["parking"])],
        "pref_area": [form_data["pref_area"]],
        "furnishing_status": [form_data["furnishing_status"]]

    })

    # Predict log(price)
    log_price = pipeline.predict(user_input)

    # Convert back to actual price
    price = np.exp(log_price)

    # Round the prediction
    predicted_price = round(float(price[0]), 2)

    # Format for display
    formatted_price = f"{predicted_price:,.2f}"

    return formatted_price