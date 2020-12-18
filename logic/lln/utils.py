from distribution import distributions_properties, distribution2idx


def urlIndex(url):
    # print("        - urlIndex")
    if "dist" not in url:
        return 0
    dist_name = url["dist"][0]
    idx = 0
    for dist in distributions_properties.keys():
        if distributions_properties[dist]["name"] == dist_name:
            idx = distribution2idx[dist]
            break
    # print("            * dist_name: ", dist_name)
    # print("            * idx: ", idx)
    return idx
