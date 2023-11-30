import json
import torch
from stactask import Task
from typing import List, Dict, Any


class LandCoverClassificationModel(torch.nn.Module):
    def __init__(self, checkpoint=None):
        self.checkpoint = checkpoint
        pass


class TrainTask(Task):
    name = "train"
    description = "This task trains the model"

    def batches(self, batch_size: int):
        l = len(self.items_as_dicts)
        for i in range(0, l, batch_size):
            yield self.items_as_dicts[i:min(i+batch_size, l)]
    
    def process(self, batch_size=100, checkpoint=None) -> List[Dict[str, Any]]:
        model = LandCoverClassificationModel()

        for i, batch in enumerate(self.batches(batch_size=batch_size)):
            print(f"Working on Batch {i+1}")

        return []


class InferenceTask(Task):
    name = "inference"
    description = "This task creates inferences for the model"

    def process(self, **kwargs) -> List[Dict[str, Any]]:
        print(kwargs)
        input_item = self.items_as_dicts[0]

        """
            TODO:
            - Take the geometry and datetime from the given input STAC item
            - Load the imagery required for this model using something like stackstac
            - Transform the imagery as needed
            - Run the model inferencing code using the transformed imagery
            - Transform the inference output as needed
            - Upload the transformed inference output to some cloud object storage
            - Return the output STAC item with the inference item as an asset
        """

        output_item = {
            "type": "Feature",
            "id": input_item["id"],
            "stac_version": input_item["stac_version"],
            "geometry": input_item["geometry"],
            "properties": {
                "datetime": input_item["properties"]["datetime"]
            },
            "links": [],
            "assets": {
                "inference": {
                    "href": "s3://foobar/inferences/id.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized"
                }
            }
        }
        return [
            output_item
        ]
    

if __name__ == "__main__":
    with open("examples/landcovernet/input/landcovernet.json", "r") as f:
        item_collection = json.load(f)

    t = TrainTask(item_collection)
    items = t.process(batch_size=100)
    print(items)