# LibraryProject: Django starter project

You can add users using the + symbol noted add next to Users.
To view your users click on 'Users.'
Clicking 'Users' will give you a list of users and their email addresses. I also gives the status of the user as staff or not.
You can reset a user password by selecting the user. You can also add user metadata, give user permissions such as staff status, superuser status groups and permisions allowed. You can also view user login/logout information.
User permissions include: Administration, Authentication and Authorization, Actions that can be taken by a user, content types e.t.c
You click forward arrow to give permission and the back arrow to revoke.
You can also view user History from the Users tab.
There are default groups like Admins, Editors, Views. You can also creae new groups by adding.
Groups give permissions to users collectively such that when you create a group you can add several users to the group to enjoy the same permisions.
A user can login with the username and password created by the superuser.

Security Measures Implemented
Used Django’s ORM and Forms to prevent SQL injection and sanitize input.

Enabled CSRF protection on all POST forms.

Enforced a strong Content Security Policy (CSP) using django-csp.

Limited external resource loading to trusted domains (e.g., Google Fonts).

Documented and commented security practices across settings and views.

Manually tested for XSS and CSRF vulnerabilities using crafted payloads.