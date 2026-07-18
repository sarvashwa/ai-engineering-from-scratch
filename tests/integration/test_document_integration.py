def test_document_integration(document_ingestion_service, vector_store):

    #Act
    document_ingestion_service.ingest_document(
        title = "FastAPI",
        content = "Paragraph 1\n\nParagraph 2",
    )


    #Assert
    chunks = vector_store.list_chunks()

    assert len(chunks) == 2

    expected_texts = {
        "Paragraph 1",
        "Paragraph 2",
    }

    actual_texts = {
        chunk.text
        for chunk in chunks
    }

    assert actual_texts == expected_texts

    expected_chunk_index = {0, 1}

    actual_chunk_index = {
        chunk.metadata["chunk_index"]
        for chunk in chunks
    }

    assert actual_chunk_index == expected_chunk_index

    assert all(
        chunk.metadata["title"] == "FastAPI"
        for chunk in chunks
    )