"""
Document API.
"""

from documents.dependencies import (
    get_document_service,
    get_storage_service,
)
from documents.schemas import (
    DocumentCreate,
    DocumentResponse,
)
from documents.service import DocumentService
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    UploadFile,
)
from storage.service import StorageService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=201,
)
def upload_document(
    title: str = Form(...),
    description: str | None = Form(
        default=None,
    ),
    file: UploadFile = File(...),
    storage_service: StorageService = Depends(
        get_storage_service,
    ),
    document_service: DocumentService = Depends(
        get_document_service,
    ),
) -> DocumentResponse:
    """
    Upload a document.
    """

    stored_file = storage_service.store(
        file,
    )

    request = DocumentCreate(
        title=title,
        description=description,
    )

    return document_service.create_document(
        request=request,
        stored_file=stored_file,
    )


@router.get(
    "",
    response_model=list[DocumentResponse],
)
def list_documents(
    service: DocumentService = Depends(
        get_document_service,
    ),
) -> list[DocumentResponse]:
    """
    List documents.
    """

    return service.list_documents()


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
)
def get_document(
    document_id: int,
    service: DocumentService = Depends(
        get_document_service,
    ),
) -> DocumentResponse:
    """
    Retrieve a document.
    """

    return service.get_document(
        document_id,
    )
