/**
 * Object Detection Evaluation (JavaScript)
 * Reference: https://mlhive.com/playground/computer-vision/algorithms/detection-metrics
 */

const IOU_THR = 0.5;
const GT = [
  { id: "gt1", class: "car", x: 0.10, y: 0.20, w: 0.25, h: 0.20 },
  { id: "gt2", class: "car", x: 0.40, y: 0.25, w: 0.20, h: 0.18 }
];
const PREDS = [
  { id: "p1", class: "car", score: 0.92, x: 0.11, y: 0.21, w: 0.24, h: 0.19 },
  { id: "p2", class: "car", score: 0.60, x: 0.80, y: 0.80, w: 0.10, h: 0.10 }
];

function iou(a, b) {
  const x1 = Math.max(a.x, b.x), y1 = Math.max(a.y, b.y);
  const x2 = Math.min(a.x + a.w, b.x + b.w), y2 = Math.min(a.y + a.h, b.y + b.h);
  const inter = Math.max(0, x2 - x1) * Math.max(0, y2 - y1);
  const union = a.w * a.h + b.w * b.h - inter;
  return union > 0 ? inter / union : 0;
}

let tp = 0, fp = 0;
const matched = new Set();

for (const p of PREDS) {
  let best = 0, bestGt = null;
  for (const gt of GT) {
    if (gt.class === p.class && !matched.has(gt.id)) {
      const o = iou(p, gt);
      if (o > best) { best = o; bestGt = gt; }
    }
  }
  if (best >= IOU_THR && bestGt) {
    matched.add(bestGt.id);
    tp++;
  } else fp++;
}

console.log("--- Detection Evaluation (JavaScript) ---");
console.log(`TP: ${tp}, FP: ${fp}, FN: ${GT.length - tp}`);
console.log(`Precision: ${(tp / (tp + fp) * 100).toFixed(1)}%`);
console.log(`Recall:    ${(tp / GT.length * 100).toFixed(1)}%`);
