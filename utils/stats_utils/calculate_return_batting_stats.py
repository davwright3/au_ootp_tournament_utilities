"""Module for calculating individual stats."""


def calculate_avg(hits, at_bats):
    """Get batting average."""
    return (hits.sum()/at_bats.sum()).round(3)


def calculate_obp(hits, bbs, hp, sf, at_bats):
    """Calculate on base percentage."""
    return ((hits.sum() + bbs.sum() + hp.sum()) /
            (at_bats.sum() + bbs.sum() + hp.sum() + sf.sum())).round(3)


def calculate_slg(tb, at_bats):
    """Calculate slugging percentage."""
    return (tb.sum() / at_bats.sum()).round(3)


def calculate_ops(obp, slg):
    """Calculate OBP + SLG."""
    return obp + slg


def calculate_woba(bbs, hp, single, double, triples, hr, at_bats, ibb, sf):
    """Calculate Woba percentage."""
    return (((.701 * bbs.sum()) + (.732 * hp.sum()) + (.895 * single.sum()) +
             (1.270 * double.sum()) + (1.608 * triples.sum()) +
             (2.072 * hr.sum())) /
            (at_bats.sum() + bbs.sum() - ibb.sum() +
             sf.sum() + hp.sum())).round(3)


def calculate_hr_rate(hr, plate_app):
    """Calculate HR RATE."""
    return ((hr.sum() / plate_app.sum())*600).round(2)


def calculate_bb_rate(bbs, plate_app):
    """Calculate BB RATE."""
    return ((bbs.sum() / plate_app.sum())*600).round(2)


def calculate_k_rate(so, plate_app):
    """Calculate K-RATE."""
    return ((so.sum() / plate_app.sum())*600).round(2)
