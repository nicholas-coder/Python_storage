"""Здесь хранятся шаблоны, на основе которых генерируются файлы. "NEW_UTILITY" - заменяется на выбранное имя"""

adc_h = ['/**', '  ******************************************************************************',
         '  * File Name          : new_utility_adc.h', '  * Date               :', '  * Description        :  ',
         '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
         '  ******************************************************************************', '  */', '',
         '/* Define to prevent recursive inclusion -------------------------------------*/',
         '#ifndef NEW_UTILITY_ADC_H', '#define NEW_UTILITY_ADC_H', '#ifdef __cplusplus', ' extern "C" {', '#endif', '',
         '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_ADC_H */',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

def_h = ['/**', '  ******************************************************************************',
         '  * File Name          : new_utility_def.h', '  * Date               :', '  * Description        :  ',
         '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
         '  ******************************************************************************', '  */', '',
         '/* Define to prevent recursive inclusion -------------------------------------*/',
         '#ifndef NEW_UTILITY_DEF_H', '#define NEW_UTILITY_DEF_H', '#ifdef __cplusplus', ' extern "C" {', '#endif', '',
         '#include "utilities_def.h"', '', '', '', '#ifdef __cplusplus', '}', '#endif',
         '#endif /* NEW_UTILITY_DEF_H */',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

gpio_h = ['/**', '  ******************************************************************************',
          '  * File Name          : new_utility_gpio.h', '  * Date               :', '  * Description        :  ',
          '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
          '  ******************************************************************************', '  */', '',
          '/* Define to prevent recursive inclusion -------------------------------------*/',
          '#ifndef NEW_UTILITY_GPIO_H', '#define NEW_UTILITY_GPIO_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
          '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_GPIO_H */',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

init_h = ['/**', '  ******************************************************************************',
          '  * File Name          : new_utility_init.h', '  * Date               :', '  * Description        : ',
          '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE ',
          '  ******************************************************************************', '  */', '',
          '/* Define to prevent recursive inclusion -------------------------------------*/',
          '#ifndef NEW_UTILITY_INIT_H', '#define NEW_UTILITY_INIT_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
          '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_INIT_H */',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

it_h = ['/**', '  ******************************************************************************',
        '  * File Name          : new_utility_it.h', '  * Date               :', '  * Description        :  ',
        '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
        '  ******************************************************************************', '  */', '',
        '/* Define to prevent recursive inclusion -------------------------------------*/', '#ifndef NEW_UTILITY_IT_H',
        '#define NEW_UTILITY_IT_H', '#ifdef __cplusplus', ' extern "C" {', '#endif', '', '', '', '',
        '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_IT_H */',
        '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

main_h = ['/**', '  ******************************************************************************',
          '  * File Name          : new_utility_main.h', '  * Date               :', '  * Description        :  ',
          '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
          '  ******************************************************************************', '  */', '',
          '/* Define to prevent recursive inclusion -------------------------------------*/',
          '#ifndef NEW_UTILITY_MAIN_H', '#define NEW_UTILITY_MAIN_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
          '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_MAIN_H */',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

sett_h = ['/**', '  ******************************************************************************',
          '  * File Name          : new_utility_sett.h', '  * Date               :', '  * Description        :  ',
          '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
          '  ******************************************************************************', '  */', '',
          '/* Define to prevent recursive inclusion -------------------------------------*/',
          '#ifndef NEW_UTILITY_SETT_H', '#define NEW_UTILITY_SETT_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
          '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_SETT_H */',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

spi_h = ['/**', '  ******************************************************************************',
         '  * File Name          : new_utility_spi.h', '  * Date               :', '  * Description        :  ',
         '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
         '  ******************************************************************************', '  */', '',
         '/* Define to prevent recursive inclusion -------------------------------------*/',
         '#ifndef NEW_UTILITY_SPI_H', '#define NEW_UTILITY_SPI_H', '#ifdef __cplusplus', ' extern "C" {', '#endif', '',
         '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_SPI_H */',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

state_h = ['/**', '  ******************************************************************************',
           '  * File Name          : new_utility_state.h', '  * Date               :', '  * Description        :',
           '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
           '  ******************************************************************************', '  */', '',
           '/* Define to prevent recursive inclusion -------------------------------------*/',
           '#ifndef NEW_UTILITY_STATE_H', '#define __UTILITY_STATE_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
           '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_STATE_H */',
           '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

tim_h = ['/**', '  ******************************************************************************',
         '  * File Name          : new_utility_tim.h', '  * Date               :', '  * Description        :  ',
         '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
         '  ******************************************************************************', '  */', '',
         '/* Define to prevent recursive inclusion -------------------------------------*/',
         '#ifndef NEW_UTILITY_TIM_H', '#define NEW_UTILITY_TIM_H', '#ifdef __cplusplus', ' extern "C" {', '#endif', '',
         '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_TIM_H */',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

uart_h = ['/**', '  ******************************************************************************',
          '  * File Name          : new_utility_usart.h', '  * Date               :', '  * Description        :  ',
          '  * COPYRIGHT(c) 2018 LLC URALENERGOSERVICE',
          '  ******************************************************************************', '  */', '',
          '/* Define to prevent recursive inclusion -------------------------------------*/',
          '#ifndef NEW_UTILITY_USART_H', '#define NEW_UTILITY_USART_H', '#ifdef __cplusplus', ' extern "C" {', '#endif',
          '', '', '', '', '#ifdef __cplusplus', '}', '#endif', '#endif /* NEW_UTILITY_USART_H */',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

adc_c = ['/**', '******************************************************************************',
         '* File Name          : new_utility_adc.c', '* Date               : ', '* Description        : ',
         '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
         '/* Includes ------------------------------------------------------------------*/',
         '#include "new_utility_def.h"', '#include "new_utility_adc.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
         '', '', '#endif /*NEW_UTILITY*/',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

gpio_c = ['/**', '******************************************************************************',
          '* File Name          : new_utility_gpio.c', '* Date               : ', '* Description        : ',
          '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
          '/* Includes ------------------------------------------------------------------*/',
          '#include "new_utility_def.h"', '#include "new_utility_gpio.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
          '', '', '#endif /*NEW_UTILITY*/',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

init_c = ['/**', '******************************************************************************',
          '* File Name          : new_utility_init.c', '* Date               : ', '* Description        : ',
          '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
          '/* Includes ------------------------------------------------------------------*/',
          '#include "new_utility_def.h"', '#include "new_utility_init.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
          '', '', '#endif /*NEW_UTILITY*/',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

it_c = ['/**', '******************************************************************************',
        '* File Name          : new_utility_it.c', '* Date               : ', '* Description        : ',
        '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
        '/* Includes ------------------------------------------------------------------*/',
        '#include "new_utility_def.h"', '#include "new_utility_it.h"', '', '#if (defined UTIL_NEW_UTILITY_EN)', '\t',
        '/* IT FLAGS MANAGE FUNCTIONS BEGIN*/', '', '/* IT FLAGS MANAGE FUNCTIONS END*/', '', '  ',
        '/* IRQ HANDLER FUNCTIONS BEGIN*/', '\t', '/* IRQ HANDLER FUNCTIONS END*/', '', '', '', '',
        '/* IRQ CALLBACK FUNCTIONS BEGIN*/', '', '/* IRQ CALLBACK FUNCTIONS END*/', '', '', '#endif /*NEW_UTILITY*/',
        '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

main_c = ['/**', '******************************************************************************',
          '* File Name          : new_utility_main.c', '* Date               : ', '* Description        : ',
          '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
          '/* Includes ------------------------------------------------------------------*/',
          '#include "new_utility_def.h"', '#include "new_utility_main.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
          '', '', '#endif /*NEW_UTILITY*/',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

spi_c = ['/**', '******************************************************************************',
         '* File Name          : new_utility_spi.c', '* Date               : ', '* Description        : ',
         '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
         '/* Includes ------------------------------------------------------------------*/',
         '#include "new_utility_def.h"', '#include "new_utility_spi.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
         '', '', '#endif /*NEW_UTILITY*/',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

tim_c = ['/**', '******************************************************************************',
         '* File Name          : new_utility_tim.c', '* Date               : ', '* Description        : ',
         '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
         '/* Includes ------------------------------------------------------------------*/',
         '#include "new_utility_def.h"', '#include "new_utility_tim.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
         '', '', '#endif /*NEW_UTILITY*/',
         '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']

uart_c = ['/**', '******************************************************************************',
          '* File Name          : new_utility_usart.c', '* Date               : ', '* Description        : ',
          '* COPYRIGHT(c) 2018 LLC URALENERGOSERVICE', '**/',
          '/* Includes ------------------------------------------------------------------*/',
          '#include "new_utility_def.h"', '#include "new_utility_usart.h"', '', '', '#if (defined UTIL_NEW_UTILITY_EN)',
          '', '', '#endif /*NEW_UTILITY*/',
          '/************************COPYRIGHT(c) 2018 LLC URALENERGOSERVICE *****END OF FILE****/']
