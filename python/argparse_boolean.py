import argparse


parser = argparse.ArgumentParser(description='Train a Fast R-CNN network')
parser.add_argument('--include_mask', 
                        help='Whether to include instance segmentations masks ',
                        default=False, type=lambda x: (str(x).lower()) == 'true')	# <<---type

args = parser.parse_args()
print(args.include_mask)
if(args.include_mask == True):
	print("True")
elif(args.include_mask == False):
	print("False")
