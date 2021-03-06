import os

def create_key(template, outtype=('nii.gz'), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return (template, outtype, annotation_classes)

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('{bids_subject_session_dir}/anat/{bids_subject_session_prefix}_run-{item:02d}_T1w')


    #Diffusion
    dwi = create_key('{bids_subject_session_dir}/dwi/{bids_subject_session_prefix}_run-{item:02d}_dwi')



    rest = create_key('{bids_subject_session_dir}/func/{bids_subject_session_prefix}_task-rest_run-{item:02d}_bold')



    info = { t1w:[], 
            dwi:[],
            rest:[]}

    for idx, s in enumerate(seqinfo):

        #t1
        if ('IR-SPGR' in s.series_description):
            info[t1w].append({'item': s.series_id})
        #rsfmri
        if ('Resting' in s.series_description):
            info[rest].append({'item': s.series_id})

        #dwi
        if ('DTI' in s.series_description ):
            info[dwi].append({'item': s.series_id})

    
              
    return info
