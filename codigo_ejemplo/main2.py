import json
import cv2

def draw_boxes_from_json(image_path, json_path):
    """Draws bounding boxes on an image based on JSON face detection results."""
    with open(json_path, 'r') as f:
        data = json.load(f)

    img = cv2.imread(image_path)

    for i in data['responses'][0]['faceAnnotations']:
        vertices = i['boundingPoly']['vertices']
        p1 = vertices[0]
        p2 = vertices[2]
        cv2.rectangle(img,(p1['x'],p1['y']),(p2['x'],p2['y']),(0,255,0),2)

    #cv2.rectangle(img, (295,111),(472,317),(0,255,0),2)
    #for face in data:
    #    vertices = face['bounding_box']
    #    cv2.rectangle(img, (vertices[0][0], vertices[0][1]), (vertices[2][0], vertices[2][1]), (0, 255, 0), 2)

    cv2.imshow('Image with Boxes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_path = 'rostros.jpg'
    json_path = 'response.json'
    draw_boxes_from_json(image_path, json_path)
