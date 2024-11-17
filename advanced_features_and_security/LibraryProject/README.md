# Introduction to Django Development Environment Setup
# Permissions and Groups Setup

This Django application utilizes custom permissions and groups to control access.

## Custom Permissions
The following permissions are defined for the `Book` model:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating new books.
- `can_edit`: Allows editing existing books.
- `can_delete`: Allows deleting books.

## Groups
The following groups are created with the corresponding permissions:
- **Viewers**: Can view books (`can_view`).
- **Editors**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`).
- **Admins**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Enforcing Permissions in Views
Permissions are enforced in the views using the `@permission_required` decorator. For example, to create a book, a user must have the `can_create` permission.
