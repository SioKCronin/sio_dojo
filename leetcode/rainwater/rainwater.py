array = [0,1,0,2,1,0,1,3,2,1,2,1]

def rain_water_calculator(array):
  
  previous_local_height = array[0]
  previous_local_idx = 0
  water_volume = 0

  def find_container_volume( k):
    for x, height in enumerate(array[k:]):
      if x == len(array[k:]) - 1:
        return (0, len(array))
      if height >= previous_local_height:
        water_volume = sum([previous_local_height - dirt_height for dirt_height in array[previous_local_idx + 1 : current_height_index + 1]])
        previous_local_height = height
        return (water_volume, previous_local_idx)

  water_volume, idx = find_container_volume(0)

  while idx < (len(array) - 1):
    tup = find_container_volume(idx)
    water_volume += tup[0]
    idx = tup[1] 
  
  return water_volume
