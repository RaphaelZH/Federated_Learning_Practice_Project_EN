import torch
from torchvision import datasets

if __name__ == "__main__":
    data_path = "/tmp/files/"

    tensor_mnist = datasets.MNIST(
        data_path, train=True, download=True, transform=transforms.ToTensor()
    )

    tensor_images = torch.stack(
        [tensor_image for tensor_image, _ in tensor_mnist], dim=3
    )

    print(tensor_images.shape)
