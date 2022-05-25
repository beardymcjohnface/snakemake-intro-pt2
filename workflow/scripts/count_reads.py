# scripts/count_reads.py
with open(snakemake.output[0],'w') as out:
    with open(snakemake.input[0],'r') as f:
        for i, l in enumerate(f):
            pass
        count = str((i + 1) / 4)
        out.write(snakemake.wildcards.sample + '\t' + count + '\n')
