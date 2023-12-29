from ansible_sdk import AnsibleJobDef
from ansible_sdk.executors import AnsibleSubprocessJobExecutor

# Declare the job executor to use.
executor = AnsibleSubprocessJobExecutor()
# Configure the job definition.
jobdef = AnsibleJobDef('datadir', 'pb.yml')
# Run the job with the executor.
job_status = await executor.submit_job(jobdef)
