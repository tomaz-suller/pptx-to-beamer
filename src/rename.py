RENAME_DICT = {
    'Aula01 - Teoria - 2022.pptx'                       : '1-teoria.pptx',
    'Aula01 - Lab - 2022.pptx'                          : '1-lab.pptx',
    'Aula02 - Teoria - 2021.pptx'                       : '2-teoria.pptx',
    'Exercício em sala 03-2022.pptx'                    : '3-exercicio.pptx',
    'Atividade da aula 4 - 2022.pptx'                   : '4-exercicio.pptx',
    'Semana 3 - aula 05 - Teoria para vídeo - 2021.pptx': '5-video.pptx',
    'Semana 3 - aula 05-06 - Teoria tudo - 2021.pptx'   : '5-6-teoria.pptx',
    'Semana 4 - aula 07-08 - Teoria tudo - 2021.pptx'   : '7-8-teoria.pptx',
    'Semana 5 - aula 09 - 2022 - Teoria.pptx'           : '9-teoria.pptx',
    'Semana 6 - aula 10 e 11 - Teoria - 2021.pptx'      : '10-11-teoria.pptx',
    'Semana 7 - aula 12 - Teoria - 2021.pptx'           : '12-teoria.pptx',
    'Semana 8 - aula 13 - Teoria - 2021.pptx'           : '13-teoria.pptx',
    'Semana 8 - aula 14 - Teoria - 2021.pptx'           : '14-teoria.pptx',
    'Semana 9 - aula 15 - Teoria - 2021.pptx'           : '15-teoria.pptx',
    'Semana 9 - aula 16 - Teoria - 2021.pptx'           : '16-teoria.pptx',
    'Semana 10 - aula 17 - Teoria - 2022.pptx'          : '17-teoria.pptx',
    'Semana 11 - aula 18 - Teoria - 2022.pptx'          : '18-teoria.pptx',
    'Semana 12 - Exercício em sala.pptx'                : '19-exercicio.pptx',
    'Questões Éticas e Temporalidade.pptx'              : 'etica.pptx',
}

if __name__ == '__main__':
    import argparse
    import shutil

    from helper import get_input_output_dir_parser

    parser = argparse.ArgumentParser(
        'Rename files based on RENAME_DICT'
    )
    parser = get_input_output_dir_parser(parser)
    args = parser.parse_args()

    for old_name, new_name in RENAME_DICT.items():
        shutil.copy(
            args.input_dir / old_name,
            args.output_dir / new_name,
        )
