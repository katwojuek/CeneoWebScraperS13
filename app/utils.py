selectors = {
    "opinion_id": (None, "data-entry-id"),
    "author": ("span.user-post__author-name",),
    "recommendation": ("span.user-post__author-recomendation > em",),
    "rating": ("span.user-post__score-count",),
    "content": ("div.user-post__text",),
    "pros": ("div.review-feature__title--positives ~ div.review-feature__item", None, True),
    "cons": ("div.review-feature__title--negatives ~ div.review-feature__item", None, True),
    "useful": ("button.vote-yes > span",),
    "useless": ("button.vote-no > span",),
    "publish_date": ("span.user-post__published > time:nth-child(1)",'datetime'),
    "purchase_date": ("span.user-post__published > time:nth-child(2)",'datetime'),
}

def extract(ancestor, selector=None, attribute=None, return_list=False):
    if selector:
        if return_list:
            if attribute:
                return [tag[attribute].strip() for tag in ancestor.select(selector)]
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if attribute:
            try:
                return ancestor.select_one(selector)[attribute].strip()
            except TypeError:
                return None
        try:
            return ancestor.select_one(selector).text.strip()
        except AttributeError:
            return None
    if attribute:
        return ancestor[attribute].strip()
    return ancestor.text.strip()