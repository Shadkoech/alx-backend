# Pagination

## Overview
This project provides functionality for paginating a dataset using various methods, including simple pagination with page and page_size parameters, hypermedia metadata, and deletion-resilient pagination.
It also touches on Sorting and filtering as methods of improving API design.

Pagination is essential when dealing with large datasets to efficiently manage and present data to users in manageable chunks. This project aims to implement pagination techniques in Python using the Popular Baby Names dataset as an example.

## Pagination methods

The project implements the following pagination methods:

1. `Simple Pagination:` Paginate the dataset using page and page_size parameters.
2. `Hypermedia Metadata:` Include hypermedia metadata in the paginated response.
3. `Deletion-Resilient Pagination:` Paginate the dataset in a deletion-resilient manner.