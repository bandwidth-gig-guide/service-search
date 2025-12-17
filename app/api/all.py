from fastapi import APIRouter, Query
from typing import Optional, List
from app.rest.search.get import get
from app.cache.redis import make_key, cache_wrap

all = APIRouter()


# GET
@all.get("/id-and-title", response_model=dict)
def get_(
    recordTypes: Optional[List[str]] = Query(default=None),
    searchString: Optional[str] = None, 
    limit: Optional[int] = 6
):
    filters = {
        "recordTypes": recordTypes,
        "searchString": searchString,
        "limit": limit
    }

    key = make_key("search:id-and-title", **filters)

    return cache_wrap(key, lambda: get(record_types=recordTypes, search_string=searchString, limit=limit),
    )
