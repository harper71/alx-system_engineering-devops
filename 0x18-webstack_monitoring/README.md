To set up monitors in Datadog to track and alert on read and write requests per second, follow these steps:

### 1. Access Datadog Dashboard
1. Log in to your Datadog account.
2. Navigate to the **Monitors** section by clicking on **Monitors** in the left-hand sidebar and then **New Monitor**.

### 2. Create Monitor for Read Requests Per Second

1. **Create a New Monitor:**
   - Click **New Monitor**.
   - Select **Metric** as the type of monitor.

2. **Configure the Monitor:**
   - **Choose a Metric**: Use the metric related to read requests. Commonly, this would be something like `system.disk.read_ops` or `disk.read_bytes` depending on how the read requests are reported.
   - **Set the Aggregation**: Choose an aggregation function such as `sum` or `rate` depending on how you want to analyze the data.
   - **Define the Query**:
     - For example, if you're using `rate`, the query might look like `rate(system.disk.read_ops{*} [1m])`.
   - **Set Alert Conditions**: Define when you want to be alerted. For instance:
     - **Threshold**: Set a threshold that triggers an alert if read requests per second exceed a certain value.
     - **Alert Conditions**: Choose whether the alert should trigger if the value is above or below the threshold.

3. **Set Notification Options:**
   - Choose how you want to be notified (e.g., email, Slack, etc.).
   - Configure the message that will be sent when the alert is triggered.

4. **Save the Monitor:**
   - Review your settings and click **Save**.

### 3. Create Monitor for Write Requests Per Second

1. **Create a New Monitor:**
   - Click **New Monitor**.
   - Select **Metric** as the type of monitor.

2. **Configure the Monitor:**
   - **Choose a Metric**: Use the metric related to write requests. Commonly, this might be `system.disk.write_ops` or `disk.write_bytes` depending on your setup.
   - **Set the Aggregation**: Choose an aggregation function such as `sum` or `rate`.
   - **Define the Query**:
     - For example, if you're using `rate`, the query might look like `rate(system.disk.write_ops{*} [1m])`.
   - **Set Alert Conditions**: Define the threshold and conditions that will trigger an alert.
     - **Threshold**: Set a threshold value for write requests per second.
     - **Alert Conditions**: Decide when to trigger the alert based on the threshold.

3. **Set Notification Options:**
   - Configure how you want to be notified and customize the alert message.

4. **Save the Monitor:**
   - Review the settings and click **Save**.

### 4. Verify Monitors

- After setting up the monitors, verify that they are working by checking the Datadog dashboard and ensuring that the alerts are triggered under the expected conditions.

By following these steps, you'll have active monitors in Datadog that alert you about the number of read and write requests per second, helping you to manage and scale your infrastructure more effectively.