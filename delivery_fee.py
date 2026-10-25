def calculate_delivery_fee(distance_km):
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    return 40 + max(0, distance_km - 1) * 10


if __name__ == "__main__":
    for distance in (1, 3, 5):
        fee = calculate_delivery_fee(distance)
        print(f"{distance} km: NT${fee}")
