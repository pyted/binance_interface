def get_asset(symbol, base_asset):
    symbol = symbol.strip()
    base_asset = base_asset.strip()
    if base_asset and symbol.endswith(base_asset):
        asset = symbol[0:-len(base_asset)]
        return asset
    else:
        return symbol
