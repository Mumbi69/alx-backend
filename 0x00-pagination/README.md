# Pagination
* Pagination is a technique used in web development and API design to break down a large set of data into smaller, more manageable chunks called pages. This is particularly useful when dealing with large datasets that would be impractical to load or display all at once. Pagination allows users or applications to navigate through the dataset one page at a time, typically by using parameters such as page number and page size.

# How to paginate a dataset with simple page and page_size parameters:
* Page Number: This parameter indicates the specific page of data that the user or application wants to retrieve.
* Page Size: This parameter determines the number of items or records to be included on each page.
> * For example, in a URL, you might have something like: GET /api/data?page=2&page_size=10, which would request the second page of data with 10 items per page.

# How to paginate a dataset with hypermedia metadata:
* Hypermedia pagination involves including metadata within the API response that provides additional information about how to navigate through the dataset. This can be achieved using hypermedia formats like HAL (Hypertext Application Language) or HATEOAS (Hypermedia as the Engine of Application State). The metadata typically includes links or instructions on how to fetch the next or previous pages.

# How to paginate in a deletion-resilient manner:
* Pagination in a deletion-resilient manner involves handling scenarios where items may be deleted or added while paginating. Two common strategies are:
* Using Cursor-based Pagination: Instead of relying on page numbers, use a cursor (e.g., a unique identifier) pointing to a specific item in the dataset. This ensures stability even if items are added or removed.
* Pagination with Timestamps: If your dataset has timestamp information, you can use it to paginate. For example, retrieve items created after a certain timestamp for each page.
