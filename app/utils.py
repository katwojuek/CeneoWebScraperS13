def extract_tag(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None

selectors = {
    "opinion_id": [None, "data-entry-id"],
    "author": ["span.user-post__author-name"],
    "recommendation":["span.user-post__author-recomendation > em"],
    "rating": ["span.user-post__score-count"],
    "verified": ["div.review-pz"],
    "post_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"],
    "vote_up": ["button.vote-yes", "data-total-vote"],
    "vote_down": ["button.vote-no", "data-total-vote"],
    "content": ["div.user-post__text"],
    "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
    "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True]
}
