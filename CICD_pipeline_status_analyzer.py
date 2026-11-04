pipelines = {
    "Build": ("Success", 10),
    "Test": ("Success", 15),
    "Security": ("Failed", 5),
    "Deployment": ("Pending", 0)
}

pipeline_success = True

for stage, details in pipelines.items():

    status, duration = details

    print("\nStage:", stage)
    print("Status:", status)
    print("Duration:", duration, "minutes")

    if status == "Failed":
        print("Error: Pipeline failed")
        pipeline_success = False

    elif status == "Pending":
        print("Waiting for execution")
        pipeline_success = False

    elif status == "Success":
        print("Stage completed successfully")

    else:
        print("Unknown pipeline status")
        pipeline_success = False

if pipeline_success:
    print("\nPipeline Status: SUCCESS")
else:
    print("\nPipeline Status: NOT COMPLETED")