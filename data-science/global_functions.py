# Global function definitions

def dvc_run(dest, dvc_file, output_files=False, dependencies=False, command=False, kwargs=None, env=ENV, use_cache=USE_CACHE):
    """ Uses DVC to generate (or reproduce) and version data files from some bash command or script.

    Args:
        dest (str):             output file destination directory
        dvc_file (str):         file name of dvc file to be tracked (without path)
        output_files ([str]):   list of output files to be cached and version controlled
        dependencies ([str]):   list of dependencies for command
        command (str):          Bash command to run. If None, uses first dependency (eg. python script)
        env (str):              Conda env to run in. Defaults to global variable ENV
        use_cache (bool):       If False runs/reproduces command using DVC. Default is global variable USE_CACHE

    Raises
        KeyboardIterrupt: If  dvc_file doesn't have correct suffix
    """

    if '.dvc' not in dvc_file:
        raise KeyboardInterrupt('dvc_file not valid dvc file')
    
    # reproduce files if using cache
    if USE_CACHE and os.path.isfile(os.path.join(dest, dvc_file)):
        print('REPRODUCING {}'.format(dvc_file))
        
        ! (cd {dest}; \
        eval "$(conda shell.bash hook)"; \
        conda activate {env}; \
        dvc repro {dvc_file})

    else: # this is first run
        dvc_call = ['dvc run', '-f', dvc_file]
        if output_files: dvc_call.extend(['-o ' + x for x in output_files])
        if dependencies: dvc_call.extend(['-d ' + x for x in dependencies])
        if command: dvc_call.append('"'+command+'"')

        ! (cd {dest}; \
        eval "$(conda shell.bash hook)"; \
        conda activate {env}; \
        {' '.join(dvc_call)}; \
        git add {dvc_file} .gitignore)
