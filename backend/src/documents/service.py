"""
Document service.
"""

from documents.exceptions import (
    DocumentNotFoundException,
    DuplicateDocumentException,
)
from documents.models import Document
from documents.schemas import (
    DocumentCreate,
    DocumentResponse,
)
from documents.unit_of_work import DocumentUnitOfWork
from storage.schemas import StoredFile


class DocumentService:
    """
    Document business logic.
    """

    def __init__(
        self,
        uow: DocumentUnitOfWork,
    ) -> None:
        self.uow = uow

    def list_documents(
        self,
    ) -> list[DocumentResponse]:
        """
        Return all documents.
        """

        documents = self.uow.document_repository.list()

        return [DocumentResponse.model_validate(doc) for doc in documents]

    def get_document(
        self,
        document_id: int,
    ) -> DocumentResponse:
        """
        Retrieve a document.
        """

        document = self.uow.document_repository.get(
            document_id,
        )

        if document is None:
            raise DocumentNotFoundException()

        return DocumentResponse.model_validate(
            document,
        )

    def create_document(
        self,
        request: DocumentCreate,
        stored_file: StoredFile,
    ) -> DocumentResponse:
        """
        Create document metadata.
        """

        if (
            self.uow.document_repository.get_by_checksum(
                stored_file.checksum,
            )
            is not None
        ):
            raise DuplicateDocumentException()

        document = Document(
            title=request.title,
            description=request.description,
            filename=stored_file.filename,
            original_filename=stored_file.original_filename,
            mime_type=stored_file.mime_type,
            file_size=stored_file.file_size,
            checksum=stored_file.checksum,
            storage_key=stored_file.key,
        )

        self.uow.document_repository.add(
            document,
        )

        self.uow.commit()

        self.uow.document_repository.refresh(
            document,
        )

        return DocumentResponse.model_validate(
            document,
        )
