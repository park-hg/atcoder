import math

def minimax(cur_h, node_idx, max_turn, scores, target_h):
  if cur_h == target_h:
    return scores[node_idx]

  if max_turn:
    return max(minimax(cur_h+1, node_idx*2, False, scores, target_h), minimax(cur_h+1, node_idx*2+1, False, scores, target_h))
  else:
    return min(minimax(cur_h+1, node_idx*2, True, scores, target_h), minimax(cur_h+1, node_idx*2+1, True, scores, target_h))

scores = [3, 5, 2, 9, 12, 5, 23, 23]

tree_height = math.ceil(math.log(len(scores), 2))
print(minimax(0, 0, True, scores, tree_height))