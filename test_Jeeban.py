#!/user/bin/env python3

from python_script_Jeeban import count_kmers
import pytest

#avoid repetition by loading data in advance 
@pytest.fixture 

def seq():	
	seq = 'ATTTGGATT'
	return seq

#test k = 6 produces 4 kmers 
def test_count_kmers(seq):
	counts = count_kmers(seq, 6)
	assert len(counts) == 4 