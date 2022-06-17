clean_intermediate:
	rm -rf ply_data
	rm -rf draco_intermediate
	rm -rf draco_output

clean: clean_intermediate
	rm -rf final_output