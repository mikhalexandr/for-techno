from fastapi import HTTPException


class CustomException(Exception):
    def __init__(
            self,
            code: int,
            status: str,
            message: str
    ):
        self.code = code
        self.status = status
        self.message = message

    def to_http_exception(
            self
    ) -> HTTPException:
        return HTTPException(
            status_code=self.code,
            detail={
                "status": self.status,
                "message": self.message
            }
        )


def handle_exception(
        e: Exception
) -> HTTPException:
    if isinstance(e, CustomException):
        raise e.to_http_exception()
    else:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "message": "Internal Server Error",
                "error": str(e)
            }
        )
