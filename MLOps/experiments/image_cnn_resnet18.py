import mlflow
import mlflow.pytorch
import torch
import torchvision
from torchvision import transforms
from torch import nn, optim


def main():
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.pytorch.autolog()

    transform = transforms.ToTensor()
    dataset = torchvision.datasets.FakeData(size=256, image_size=(3, 224, 224), num_classes=10, transform=transform)
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

    model = torchvision.models.resnet18(num_classes=10)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters())

    for epoch in range(1):
        for images, labels in dataloader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

if __name__ == "__main__":
    main()
