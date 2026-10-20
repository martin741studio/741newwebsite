# Add, edit, and delete Analytics users and user groups

- URL: https://support.google.com/analytics/answer/9305788?hl=en
- Fetched: 2026-10-12
- Page date: living help page (no date shown)
- Author/site: Google (support.google.com help center)

---

*If you're switching from Universal Analytics to Google Analytics, use the**migration tool** to copy users to your new Google Analytics property.*

You can add users at the Analytics account or property level. The level at which you add a user determines that user's initial access. For example, if you add a user at the account level, then that user also has access to all the properties in the account, with the same set of permissions. If you add a user at the property level, then the user has access to only that property with the permissions you provide. You can change the level of access and permissions for a user at any time. Learn more about Access and data-restriction management.

Users are identified by their email addresses. You can only add users whose email addresses are registered in Google accounts.

To add or modify users or user groups, you need to have the Administrator role at the account or property level. You can add or modify users or user groups at each level for which you have permission.

To delete user accounts or user groups, you need to have the Administrator role at the account level. You can delete users or user groups only at the account level.

Any user with permission can delete any other user. As a safety measure, if you are the last user who has the Administrator role, you cannot delete yourself.

While you manage users for subproperties and roll-up properties the same way you do for any other property, there are some differences in the effects of that user management. Learn more about users in subproperties and roll-up properties.

**On this page**

## Add users to Analytics

You can add as many users as you need. To add a new user to an account or property:

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. In the “Account or Properties permissions” list, click **+**, then click **Add users**.
3. Enter the email address for the user's Google Account or Google Workspace Account.
4. Select **Notify new users by email** to send a message to the user.
5. Select the permissions you want. Learn more about permissions.
6. Click **Add**.

The Google email address you use to add a user and the password associated with that address become the Analytics login credentials for that user.

Search the user list, or click  **> Add filter** to filter the list, for user names, email addresses, Org admins, user groups, permissions, or policy violations.

## Edit users

You can edit the permissions for any user at any level in an Analytics account. For example, if you have given a user the *Viewer* role for only a single property, you can subsequently also give the user the *Editor* role for only that property. Or you can give that user the *Editor* role at the account level, and thereby also give them the *Editor* role for every property in that account.

You can give a user more permissions as you move down the account hierarchy, but you cannot give a user fewer permissions than you assigned at higher levels. For example, if you assign a user the *Editor* role at the account level, then that user also has the *Editor* role at the property level (and you cannot revoke those permissions at the property level). Conversely, you can assign a user the *Editor* role at the property level, but assign no permissions the account level. Learn more about Access and data-restriction management.

To modify permissions for an existing user:

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. Use the search box at the top of the list to find the user you want. Enter a full or partial address.
    
  - For example, janedoe@gmail.com or janedoe
3. Click the user name, then add or remove permissions.
4. Click **Save**.

## Delete users

To delete a user:

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. Use the search box at the top of the list to find the user you want. Enter a full or partial address.
    
  - For example, janedoe@gmail.com or janedoe
3. Select the check box for each user you want to delete, then click **REMOVE**.

If you remove a user from a source property, that user is also removed from its subproperties.

If you remove a user from a subproperty, that user is removed from only the subproperty.

Learn more about users in subproperties.

## Create user groups

You can create user groups with permissions for your Analytics account.

To create a user group, your Analytics account has to belong to an organization. If your account doesn't belong to an organization, Analytics walks you through that process of creating and linking to an organization when you create your first user group. Learn more about User groups.

To create a user group:

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. In the "Account or Properties permissions" list click **+**, then click **Add user groups**.
3. Click **Add group**.
4. Click **+**, enter a name and description for the group, then click **CREATE**.
5. Select the permissions you want, then click **ADD**. Learn more about Access and data-restriction management.

After you create a group, it appears in the users lists for your Analytics account and for your organization.

The group has permissions for the level in the Analytics hierarchy where you create the group. For example, if you create the group at the property level, then it has permissions only for that property. If you create it at the account level, then it has permissions for all properties. Refer to Edit user groups below for information about adding permissions to other levels of the Analytics hierarchy.

## Add users to a group

To add users to a group:

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. Use the search box at the top of the list to find the user group you want. Enter a full or partial group name.
3. In the row for that group, click , then click **View group's organization details**.
4. Click **Members**, then click **+**.
5. Enter the email addresses of the users you want to add.
6. If you want to add other groups to this group, click **ADD GROUP**.
7. After you have added the users and groups you want, click **ADD**.
8. Close the *Members* panel, and close the panel for the group.
9. Click **Save**.

### Add a user group to a level of your Analytics hierarchy

After you create a group, you can add it to any level of your Analytics hierarchy in order to give all users in the group permissions for that level.

1. In **Admin**, under "Account" or "Property", click **Access Management**.
2. In the users list, click **+**, then click **Add user groups**.
3. Click **ADD GROUP**.
4. Select the group you want, then click **DONE**.

## Edit user groups

After you create a user group, you can add and remove users, groups, and permissions; and you can add the group to other groups.

To edit a user group:

1. In **Admin** under "Account" or "Property", click **Access Management**.
2. Use the search box at the top of the list to find the user group you want. Enter a full or partial group name.
3. In the row for that group, click , then click **View group's organization details**.
4. To add users or user groups, click **Members**, then click **+**. After you add members, click **ADD**.
5. To add the group to other groups, click **Group memberships**, then click **+**. After you choose groups, click **DONE**.
6. To give the group permissions for other levels of your Analytics hierarchy, such as properties and views:
    
  - Click **Analytics**.
  - Expand the hierarchy, and click for each level where you want to modify permissions.
  - Select the permissions you want to add, then click **SAVE**.

Use the same procedure to remove users from the group, remove the group from other groups, or to modify permissions. Learn more about User groups.
