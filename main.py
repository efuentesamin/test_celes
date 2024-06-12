import uvicorn
from decouple import config
from shared_kernel.database import Base, engine

PORT = config('PORT', default=8080, cast=int)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run("app.api:app", host="0.0.0.0", port=PORT, reload=True)
