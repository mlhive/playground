/**
 * Non-Maximum Suppression (NMS) in JavaScript
 * Reference: https://mlhive.com/playground/computer-vision/algorithms/non-maximum-suppression
 */

const CONF_THR = 0.3;
const IOU_THR = 0.5;
const CLASS_AWARE = true;

const BOXES = [
  { id: "A", classId: "person", score: 0.95, x: 0.14, y: 0.13, width: 0.30, height: 0.68 },
  { id: "B", classId: "person", score: 0.87, x: 0.16, y: 0.15, width: 0.30, height: 0.68 },
  { id: "C", classId: "person", score: 0.58, x: 0.12, y: 0.11, width: 0.31, height: 0.70 },
  { id: "D", classId: "dog",    score: 0.92, x: 0.55, y: 0.40, width: 0.28, height: 0.45 },
  { id: "E", classId: "dog",    score: 0.64, x: 0.58, y: 0.42, width: 0.25, height: 0.42 }
];

function iou(a, b) {
  const x1 = Math.max(a.x, b.x), y1 = Math.max(a.y, b.y);
  const x2 = Math.min(a.x + a.width, b.x + b.width), y2 = Math.min(a.y + a.height, b.y + b.height);
  const inter = Math.max(0, x2 - x1) * Math.max(0, y2 - y1);
  const union = a.width * a.height + b.width * b.height - inter;
  return union > 0 ? inter / union : 0;
}

let pending = BOXES.filter(b => b.score >= CONF_THR).sort((a, b) => b.score - a.score);
const kept = [];

while (pending.length > 0) {
  const selected = pending.shift();
  kept.push(selected);
  pending = pending.filter(b => {
    const sameClass = (b.classId === selected.classId);
    return !(sameClass && iou(selected, b) > IOU_THR);
  });
}

console.log("--- NMS (JavaScript) ---");
console.log("Final Kept Boxes:", kept.map(b => `${b.id} (${b.classId})`));
