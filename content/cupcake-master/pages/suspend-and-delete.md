Title: Suspending and deleting instances
Order: 06
Summary: Stopping an instance for a while, deleting it, and recovering it before it is gone.
Screens: dashboard:instance_detail

## Suspend and resume

**Suspend** stops an instance's programs but keeps its data. Confirm when asked.

![](shot:steps-suspend-resume/1-suspending)

A suspended instance shows **Resume** instead.

![](shot:steps-suspend-resume/2-suspended)

**Resume** starts it again; it is active once its programs answer.

![](shot:steps-suspend-resume/3-resumed)

## Deleting an instance

Only staff can delete an instance. **Delete instance** is at the bottom of its page and says what is removed and when.

![](shot:steps-delete-instance/1-warning)

Type the instance's slug to confirm; the button only works once it matches.

![](shot:steps-delete-instance/2-confirm)

The instance is stopped at once and kept for 7 days. Its owner is told the date.

![](shot:steps-delete-instance/3-scheduled)

![](shot:steps-delete-instance/4-listed)

Backups already made are kept. The slug and the instance's domains stay reserved.

## Recovering a deleted instance

Until the date shown, staff can choose **Recover**, which cancels the deletion and starts the instance again. Its owner
cannot resume it while it is waiting to be deleted.

![](shot:steps-delete-instance/5-recovered)

## Deleting at once

To delete without waiting, type the slug again under the date and choose **Delete now**.

![](shot:steps-delete-instance/6-delete-now)

Once deleted, its programs, database and files are gone; the page keeps its history.

![](shot:steps-delete-instance/7-deleted)
