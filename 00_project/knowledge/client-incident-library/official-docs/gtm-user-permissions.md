# Managing users and permissions

- URL: https://support.google.com/tagmanager/answer/6107011?hl=en
- Fetched: 2026-10-12
- Page date: living help page (no date shown)
- Author/site: Google (support.google.com help center)

---

Google Tag Manager allows you to delegate access to other users at the account and container level.

At the account level, users can be granted the ability to view or administer the account. At the container level, users can be granted read, edit, approve, or publish rights.

You may only delegate access to Google accounts. These might be Gmail accounts, accounts managed through organizations using Google Workspace, or other accounts created at accounts.google.com.

**Note**: If your account has only one administrator, you may lose access to your tags if that user becomes unavailable. To ensure uninterrupted management, we recommend adding at least one additional administrator to your account. You’ll notice a Tag Diagnostics notification if your account is identified as having only one admin.

Additionally, make sure your account is managed by someone in your organization, not an external agency

## Add users to an account

To *add* users to a Tag Manager account:

1. Click **Admin**.
2. In the ***Account*** column, select **User Management**.
3. Click.
4. Select **Add users**.
5. Enter one or more email addresses.
6. Set **Account Permissions**. ***User*** is selected by default, and this level allows the user to view basic account information. Select ***Administrator*** if the user should have the ability to create new containers and modify user permissions for accounts and containers.
7. *Optional*: Set **Container permissions** for each container that you would like the user to have access to.
8. Click **Invite**. Each invited user will receive an invitation to use the container.

## Edit users on an account

To *edit* an existing user on a Tag Manager account:

1. Click **Admin**.
2. In the ***Account*** column, select **User Management**.
3. Select an entry in the **Account permissions** list. You can use the search and filter tools at the top of the page to narrow down results.
4. Modify account permissions as necessary.
5. To modify individual container permissions, clickand select the desired options. Click **Save** to continue.
6. If you wish to remove this user from access to the current container, click **Remove**.
7. Click **Save** to save your changes.

## Add users to a container

To add user permissions for a specific container:

1. Click **Admin**.
2. In the ***Container*** column, select **User Management**.
3. Click.
4. Select **Add users**.
5. Enter one or more email addresses.
6. Assign ***Container permissions***.
7. Click Invite. Each invited user will receive an invitation to use the container.

## Edit user access to a container

To edit user permissions for a specific container:

1. Click **Admin**.
2. In the ***Container*** column, select **User Management**.
3. Select an entry from the **Container permissions** list.
4. Modify container permissions as necessary.
5. If you wish to remove this user from access to the current container, click **Remove**.
6. Click **Save** to save your changes.

## Invitations

If a Tag Manager administrator has added a user to a Tag Manager account, that user will receive an invitation to access the account. The invited user will be notified via email, and an ***Invitations*** card will appear on Tag Manager's Accounts screen. Click the Invitations card to view the list of invitations. Expand an invitation entry to view the details of the invitation. Click **Accept** to accept the invitation, or **Decline** to cancel the invitation.

## Account permissions

Account permissions at the account level can be set to either **Admin** or **User**. You may also fine-tune permissions for specific containers on the ***Container permissions*** table.

## Container permissions

Access can be assigned on a per-container basis. For a given container, a user may be assigned:

- ***No access*:** The user will not see the container listed in the account.
- ***Read*:** The user will see the container listed and may browse the tags, triggers, and variables in the container, but will not have the ability to make any changes.
- ***Edit*:** The user has rights to create workspaces and make edits but not create versions or publish.
- ***Approve*:** The user has rights to create versions, workspaces, and make edits but not publish.
- ***Publish*:** The user has full rights to create versions, workspaces, make edits, and publish.

*"inherited"*if it is received indirectly from another place, such as a user group or organization role. A permission is considered

*"direct"*if it is assigned specifically to the user. Direct permissions will persist even if the user loses an inherited permission.

## Recovering a Google Tag Manager account

Google Tag Manager enforces a strict policy against circumventing the in-product permissions. You could end up in a scenario where nobody in your organization has access to Tag Manager because you can not send a request to our support team to add users.

Tag Manager **does not allow** all admins to be removed - trying to do so results in an error. However, if a Tag Manager account has **only one admin** and that admin's Google user account is deleted elsewhere, Tag Manager **cannot** prevent that the account will be left **without** an admin.

To avoid getting locked out:

- Configure multiple administrators and actual user accounts instead of using shared logins, see instructions above.
- Make sure that your Google accounts are managed by someone within your organization, not an outside agency or consultant.
- If you use the Google Marketing Platform: Link your Tag Manager account to your organization to get improved user management capabilities, for example, Seeing which users have access, Setting user policies, and more.

### If your account has no admin

When an account or container has **no admin,** it will be automatically deleted. Remaining users with read access have **30 days** to export their information from the trash can. If nobody in the account has read access, you must start over and retag the site.

To recover your Tag Manager container:

1. Export the container from the trash can, see Exporting information from the trash can.
2. Import the container into a new Google Tag Manager account where people in your organization have admin rights. See Import a container.
3. Ensure that you assign enough people with admin status, as recommended above.

## Users managed by the Google Marketing Platform

|  | *This feature is only available in Google Tag Manager 360, which is included in the Google Marketing Platform.* | 

Google Marketing Platform includes a centralized user management system for Google Analytics, Tag Manager, and Optimize accounts. You can assign user group permissions for an organization and for individual product accounts within the organization.

In the Google Marketing Platform, members of a user group will inherit that group's permissions. For Google Marketing Platform accounts that use Google Tag Manager:

- Users with the *Admin* permission at the account level inherit *Read* permission for all containers in that account, and can assign themselves additional permissions as necessary.
- Users who have *User* permission at the account level do not inherit any container permissions. Permissions must be assigned by an *Admin* for each container.

Learn more about Google Marketing Platform's user roles and permissions.
