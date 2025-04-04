import torch # type: ignore
import torchvision.transforms as transforms # type: ignore
from PIL import Image
import os
from django.conf import settings


classer = [
    'Bình Thường',
    'Nấm đốm',
    'Phấn Trắng',
]

mean = [0.4363, 0.4328, 0.3291]
std = [0.2129, 0.2075, 0.2038]

image_transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(torch.Tensor(mean), torch.Tensor(std))
])

def get_classify(image_url):
    image = Image.open(image_url)
    image = image_transform(image).float()
    image = image.unsqueeze(0)
    file_path = os.path.join(settings.MEDIA_ROOT, 'best_model.pth')
    # model = torch.load(os.path.join(os.path.dirname(__file__), 'best_model.pth', weights_only=True))
    model = torch.load(file_path, weights_only=False)
    model.eval()
    
    outputs = model(image)
    _, predicted = torch.max(outputs.data, 1)
    
    classification = classer[predicted.item()]
    return classification