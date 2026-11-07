pipeline = {
    "Code": "success",
    "Build": "success",
    "Test": "failed",
    "Docker": "success",
    "Deployment": "failed"
}

for stage, status in pipeline.items():

    print(stage, ":", status)

    if status == "failed":
        print("Pipeline stopped!")
        print("Failure detected at:", stage)
        break

else:
    print("\nPipeline completed successfully!")