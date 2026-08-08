import {
    CurrencyDollarIcon,
    ShoppingBagIcon,
    FireIcon,
    TrophyIcon,
} from "@heroicons/react/24/solid";

type Props = {
    title: string;
    value: string | number;
    subtitle?: string;
};

export default function StatCard({
    title,
    value,
    subtitle,
}: Props) {

    const getIcon = () => {
        switch (title) {

            case "Revenue":
                return (
                    <CurrencyDollarIcon className="w-8 h-8 text-green-600" />
                );

            case "Orders":
                return (
                    <ShoppingBagIcon className="w-8 h-8 text-blue-600" />
                );

            case "Pizzas Sold":
                return (
                    <FireIcon className="w-8 h-8 text-orange-600" />
                );

            case "Best Seller":
                return (
                    <TrophyIcon className="w-8 h-8 text-yellow-600" />
                );

            default:
                return null;
        }
    };

    const getBorderColor = () => {

        switch (title) {

            case "Revenue":
                return "border-l-green-500 bg-green-50";

            case "Orders":
                return "border-l-blue-500 bg-blue-50";

            case "Pizzas Sold":
                return "border-l-orange-500 bg-orange-50";

            case "Best Seller":
                return "border-l-yellow-500 bg-yellow-50";

            default:
                return "border-l-slate-400 bg-white";
        }

    };

    return (

        <div
            className={`
                ${getBorderColor()}
                border-l-8
                rounded-2xl
                shadow-lg
                hover:shadow-2xl
                hover:-translate-y-1
                transition-all
                duration-300
                h-[170px]
                p-6
                flex
                justify-between
                items-center
            `}
        >

            {/* Left Side */}

            <div className="flex-1">

                <p className="text-xs uppercase tracking-wider text-gray-500 font-semibold">
    {title}
</p>

                <h2
    className={`
        mt-2
        text-slate-900
        font-bold
        leading-tight
        ${
            title === "Best Seller"
                ? "text-2xl"
                : "text-4xl"
        }
    `}
>
    {value}
</h2>

                {subtitle && (

                    <p className="mt-2 text-sm text-gray-500">

                        {subtitle}

                    </p>

                )}

            </div>

            {/* Right Side */}

            <div
                className="
                    w-16
                    h-16
                    rounded-full
                    bg-white
                    shadow-md
                    flex
                    items-center
                    justify-center
                    ml-4
                    shrink-0
                "
            >

                {getIcon()}

            </div>

        </div>

    );

}