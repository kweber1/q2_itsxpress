import os

import subprocess

from nose.tools import assert_raises

from q2_types.per_sample_sequences import SingleLanePerSamplePairedEndFastqDirFmt

import itsxpressqiime2.main as itsxq

TEST_DIR = os.path.dirname(os.path.abspath(__file__))

def test_view_artifcat_type():
    testfile = os.path.join(TEST_DIR, "test_data","paired.qza","45cf54a-bf06-4852-8010-13a60fa1598c","data")
    os.chdir(testfile)
    exp1 = itsxq._view_artifact_type()
    assert exp1 == "SampleData[PairedEndSequencesWithQuality]"
    testfile2 = os.path.join(TEST_DIR, "test_data","pairedbroken.qza","45cf54a-bf06-4852-8010-13a60fa1598c","data")
    os.chdir(testfile2)
    assert_raises(subprocess.CalledProcessError, itsxq._view_artifact_type)

def test_amount_of_files_in_data():
    testfile = os.path.join(TEST_DIR, "test_data", "paired.qza","45cf54a-bf06-4852-8010-13a60fa1598c", "data")
    exp1 = itsxq._amount_of_files_in_data(str(testfile))
    assert exp1 == 4
    testfile2 = os.path.join(TEST_DIR, "test_data","pairedbroken.qza","45cf54a-bf06-4852-8010-13a60fa1598c","data")
    exp2 = itsxq._amount_of_files_in_data(str(testfile2))
    assert exp2 == 0

def test_fastq_id_maker():
    testfile = os.path.join(TEST_DIR, "test_data", "paired.qza")
    test_data = SingleLanePerSamplePairedEndFastqDirFmt(testfile, "r")
    exp1 = itsxq._fastq_id_maker(test_data)
    assert exp1 == ["4474-1MSITS3_0_L001_R1_001.fastq.gz","4474-1MSITS3_0_L001_R2_001.fastq.gz"]

def test_set_fastq_files():
    testfile = os.path.join(TEST_DIR, "test_data", "paired.qza")
    test_data = SingleLanePerSamplePairedEndFastqDirFmt(testfile, "r")
    exp1,exp2,exp3 = itsxq._set_fastq_files("SampleData[PairedEndSequencesWithQuality]", test_data)
    assert exp1 == os.path.join(TEST_DIR, "test_data", "paired.qza","45cf54a-bf06-4852-8010-13a60fa1598c", "data", "4474-1MSITS3_0_L001_R1_001.fastq.gz")
    assert exp2 == os.path.join(TEST_DIR, "test_data", "paired.qza", "45cf54a-bf06-4852-8010-13a60fa1598c", "data","4474-1MSITS3_0_L001_R2_001.fastq.gz")
    assert exp3 == False

def test_taxa_prefix_to_taxa():
    exp1 = itsxq._taxa_prefix_to_taxa("A")
    assert exp1 == "Alveolata"