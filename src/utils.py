def get_cluster_profile(cluster_id: int) -> str:
    """Return human-readable profile for each cluster"""
    profiles = {
        0: "High-income urban retailer with high digital literacy and frequent transactions.",
        1: "Rural agricultural MSME with moderate income but lower digital comfort.",
        2: "Small service business in secondary cities, price-sensitive, occasional borrower.",
        3: "Growing manufacturing MSME with high savings rate and strong engagement."
    }
    return profiles.get(cluster_id, "General MSME user")