
class ProcessedRecipe(BaseModel):
    id: str
    title: str
    ingredients: List[str]
    instructions: List[str]   # ✅ Changed from `str` to `List[str]`
    cuisine: str
    tags: List[str]
    url: str
